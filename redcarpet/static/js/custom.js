const ITEMS_PER_PAGE = 1;

var Pagination = React.createClass({
    changePage: function (event) {
        var parentClass = event.target.parentNode.className;
        if (parentClass.indexOf("disabled") > -1)
            return false;
        console.log(parentClass);
        this.props.changePage(parentClass == "previous" ? this.props.current_page - 1 : this.props.current_page + 1);
    },
    render: function () {
        var page = this.props.current_page;
        var max_page = Math.ceil(this.props.totalItems / ITEMS_PER_PAGE);
        console.log(this.props.totalItems);
        return (
            <nav>
                <ul className="pager">
                    { page > 1 &&
                    <li className="previous">
                        <a href="#" onClick={this.changePage}>Previous</a>
                    </li>
                    }
                    { page <= 1 &&
                    <li className="previous disabled">
                        <a onClick={this.changePage}>Previous</a>
                    </li>
                    }
                    { page < max_page &&
                    <li className="next">
                        <a href="#" onClick={this.changePage}>Next</a>
                    </li>
                    }
                    { page >= max_page &&
                    <li className="next disabled">
                        <a className="disabled" onClick={this.changePage}>Next</a>
                    </li>
                    }
                </ul>
            </nav>
        );
    }
});


var Field = React.createClass({
    getInitialState: function () {
        return {page: 1};
    },
    changePage: function (page) {
        console.log(page);
        this.setState({page: page})

    },
    render: function () {
        var fields = [];
        for (var key in this.props.fields) {
            fields.push(<div><h4 className="media-heading">{key}</h4>

                <p>{this.props.fields[key]}</p></div>);
        }
        var page = this.state.page;
        return (
            <div className="media-body">
                { fields.slice((page - 1) * ITEMS_PER_PAGE, page * ITEMS_PER_PAGE) }
                <Pagination current_page={page} changePage={this.changePage} totalItems={fields.length}/>
            </div>
        );
    }
});


var Thumbnail = React.createClass({
    render: function () {
        return (
            <div className="media-left">
                <a href="#">
                    <img className="media-object" src={this.props.thumbnail} height="160" width="160"/>
                </a>
            </div>
        );
    }
});


var Panel = React.createClass({
    componentDidMount: function () {
        $.ajax({
            url: "api/data",
            dataType: 'json',
            success: function (data) {
                this.setState({data: data});
            }.bind(this),
            error: function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    getInitialState: function () {
        return {data: []};
    },
    render: function () {
        return (
            <div className="panel panel-default">
                <div className="panel-heading">
                    <h3 className="panel-title">Details</h3>
                </div>
                <div className="panel-body">
                    <div className="media">
                        <Thumbnail thumbnail={this.state.data["thumbnail"]}/>
                        <Field fields={this.state.data["fields"]}/>
                    </div>
                </div>
            </div>
        );
    }
});

ReactDOM.render(<Panel />, document.getElementById("content"));