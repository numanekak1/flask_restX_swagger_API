from flask_restx import Resource, Namespace

ns= Namespace(name="Basic api",path='/api/v1/')

@ns.route('/hello')
class Hello(Resource):
    def get(self):
        return {"status":"get"}
    def post(self):
        return {"status":"post"}