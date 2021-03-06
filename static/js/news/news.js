"use strict";

const vm = new Vue({
    delimiters: ['[[', ']]'],
    el : '#app',
    data : {
        news : []
    },
    methods : {
        getNews : function() {
            var self = this;
            var search = document.getElementById("query").value;
            var endpoint = '/news/api/';
            $.ajax({
                method: "GET",
                url: endpoint,
                data: {
                    search: search
                },
                success: function (data) {
                    // console.log(data);
                    self.news = data;
                },
                error: function (error_data) {
                    alert("失敗");
                    // console.log(error_data);
                }
            });
        }
    }
});