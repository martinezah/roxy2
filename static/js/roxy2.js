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
            $scope.item = null;
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
                            $scope.status = null;
                        } else {
                            $scope.status = "No results";
                        }
                    });
                }
           }
        });
    };

    $scope.update_location_hash = function() {
        if (window.location.hash.substring(1) == $scope.query_url) {
            $scope.get_artifacts();
        } else {
            window.location.hash = $scope.query_url;
        }
    };

    $scope.on_enter_update_location_hash = function($event) {
        if ($event.keyCode == 13) {
            $scope.update_location_hash();
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

    $scope.first = function() {
        $scope.curr = 1;
        $scope.get_artifact();
    };

    $scope.last = function() {
        $scope.curr = $scope.artifacts.length;
        $scope.get_artifact();
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
        if ($scope.item.preview) {
            $scope.item.preview = false;
            $("#preview").contents().find('html').empty();
        } else {
            $scope.item.preview = true;
            $("#preview").css({"height":$("#html").height(), "width":$("#html").width()});
            $("#preview").attr("sandbox", "allow-same-origin");
            $("#preview").contents().find('html').html($scope.item.response.body);
            $("#preview").attr("sandbox", "");
        }
    };
}]);
