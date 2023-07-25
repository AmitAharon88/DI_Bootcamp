import React from 'react';

class ErrorBoundary extends React.Component {
    constructor () {
        super();
        this.state = {
            hasError: null,
            errorInfo: ''
        }
    };

    componentDidCatch(err, errorInfo) {
        console.log(err);
        this.setState({
            hasError: true,
            errorInfo: errorInfo
        })
    };

    render () {
        if (this.state.hasError) {
            return (
                <details style={{ whiteSpace: 'pre-wrap' }}>
                    {this.state.hasError && this.state.hasError.toString()}
                    <br />
                    {this.state.errorInfo.componentStack}
                </details>
            );
        };
        return this.props.children;
    };

};

export default ErrorBoundary;