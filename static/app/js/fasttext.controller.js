(function() {
    'use strict';

    angular.module(['fast-text'])
        .component('fastText', {
            templateUrl: "views/fasttext.tpl.html",
            controller: FastTextController,
            controllerAs: "ft"
        });

    function FastTextController($http, $scope) {
        var vm = this;

        vm.formsubmit = true;
        vm.showresults = false;
        vm.title = "";
        vm.text = "";
 
        vm.submit = function() {
            var content = {
                title: vm.title,
                text: vm.text
            };
            $http.post('/api/classify_text', {content: content})
                .then(function(response){
                    vm.formsubmit = true;
                    vm.showresults = true;
                    vm.status = response.data.status;
                    vm.prediction = response.data.prediction;
                });
        };
        
    }

}());
