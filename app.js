app = new Vue({
    el: '#app',
    created() {
        this.fetchData();
    },
    data: {
        categories: [],
        selected: '',
        series: [],
    },
    computed: {
        // a computed getter
        misseries: function() {
            console.log(this.selected);
            console.log('http://localhost:8000/series/' +this.selected);
            if (this.selected != '') {
                axios.get('http://localhost:8000/series/' +this.selected).then(response => {
                    console.log(this.series);
                    this.series = response.data;
                });
            }

            return this.series;
        },
    },
    methods: {
        fetchData() {
            axios.get('http://localhost:8000/categories').then(response => {
                this.categories = response.data.categories;
            });

        },

        onChange(value) {
             if (this.selected != '') {
                 axios.get(concat('http://localhost:8000/series/', this.selected)).then(response => {
                     this.series = response.data;
                 });
             }
         }
    }
});
