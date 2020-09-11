var app = new Vue({
    el: '#monitorframe',
    delimiters: ['${','}'],
    data:
    {
        interval: null,
        metrics: null,
        ready: false
    },
    mounted: function () {
        this.interval = window.setInterval(this.getParameters, 1000);
    },
    beforeDestroy: function () {
        window.clearInterval(this.interval);
    },
    computed: {
    },
    methods:
    {
        getParameters: function()
        {

            axios.get('/api')
                .then((response) => {

                    this.metrics = response.data.metrics;
                    this.ready = true;
                    console.log("Metrics received!")
                })
                .catch((err) => {
                    this.ready = false;
                    console.log(err);
                })
                    
        }
    }
});