from website import create_app


app = create_app()
# app.config['SECRET_KEY'] = 'SDKFJSDFOWEIOF'

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=5000)
    #app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)