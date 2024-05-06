from flask_restx import Resource, Namespace

# Local Modules
from .models import Course,Student
from .api_models import course_model,student_model
ns= Namespace(name="Basic api",path='/api/v1/')

@ns.route('/hello')
class Hello(Resource):
    def get(self):
        return {"status":"get"}
    def post(self):
        return {"status":"post"}
    

@ns.route('/courses')
class CourseAPI(Resource):
    @ns.marshal_list_with(course_model) #taking output and return serialised way
    def get(self):
        return Course.query.all()
    

@ns.route('/students')
class StudentAPI(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()
    