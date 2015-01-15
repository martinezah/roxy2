var roxyApp = angular.module('roxyApp', []);
roxyApp.controller('indexController', ['$scope', '$timeout', function indexController($scope, $timeout) { 
    window.scope = $scope;

    $scope.api_url = "";
    $scope.query_url = "";
    
    $scope.get_artifacts = function() {
        $timeout(function() {
            $scope.status = "Loading...";
            $scope.curr = null;
            $scope.artifacts = [];
        });
        $scope.nonce = Math.random().toString(36).replace(/[^a-z0-9]+/g, '').substr(0, 6);
        $.get($scope.api_url, {url:$scope.query_url, nonce:$scope.nonce}, function(response) {
            if (response && response.nonce == $scope.nonce) {
                if (Array.isArray(response.data)) {
                    $timeout(function() {
                        $scope.artifacts = response.data;
                        if ($scope.artifacts.length) {
                            $scope.curr = 1;
                            $scope.get_artifact();
                        }
                        $scope.status = null;
                    });
                }
           }
        });
    };

    $scope.on_enter_get_artifacts = function($event) {
        if ($event.keyCode == 13) {
            $scope.get_artifacts();
        }
    }

    $scope.get_artifact = function() {
        $timeout(function() {
            $scope.status = "Loading...";
        });
        $scope.nonce = Math.random().toString(36).replace(/[^a-z0-9]+/g, '').substr(0, 6);
        var key = $scope.artifacts[$scope.curr-1];
        if (key) {
            $scope.item_url = "/artifacts/" + key;
            $.get($scope.api_url, {url:$scope.item_url, nonce:$scope.nonce}, function(response) {
                if (response && response.nonce == $scope.nonce) {
                    $timeout(function() {
                        $scope.item = response.data;
                        try  {
                            $scope.item.response.body = $scope.item.response.body.trim();
                        } catch(err) { console.log(err); }
                        $scope.status = null;
                    });
                }
            });    
        }
    };

    $scope.prev = function() {
        if ($scope.curr > 1) {
            $scope.curr -= 1;
            $scope.get_artifact();
        }
    };

    $scope.next = function() {
        if ($scope.curr < $scope.artifacts.length) {
            $scope.curr += 1;
            $scope.get_artifact();
        }
    };

    $scope.render = function() {
        var preview_window = window.open('','preview','height=900,width=1100');
        if (window.focus) {
            preview_window.document.write($scope.item.response.body);
            preview_window.focus();
        }
    };
}]);
