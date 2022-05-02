module.exports = {
    devServer: {
        proxy: {
            // detail: https://cli.vuejs.org/config/#devserver-proxy
            '/api': {
                target: `http://127.0.0.1:8123/api`,
                changeOrigin: true,
                pathRewrite: {
                    '^/api': ''
                }
            },
            '/media': {
                target: `http://127.0.0.1:8123/media`,
                changeOrigin: true,
                pathRewrite: {
                    '^/media': ''
                }
            }
        }
    }
};