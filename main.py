from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)  # Важно: передать app

courses = {
    1: {'name': 'First cours', 'videos': 12}, 
    2: {'name': 'Second course', 'videos': 10}, 
    3: {'name': 'bla-bla', 'videos': 1}
}

class Main(Resource):
    def get(self):
        return {'info': 'some info', 'num': 56}
    

    
class Courses(Resource):
    def get(self, course_id):
        if course_id == 0:
            return courses
        else:
            return courses[course_id]
        
    def delete(self, course_id):
        del courses[course_id]
        return courses
    
api.add_resource(Main, '/api/main')
api.add_resource(Courses, '/api/courses/<int:course_id>')


if __name__ == '__main__':  # Двойное подчеркивание с двух сторон
    app.run(debug=True, port=3000, host='127.0.0.1')