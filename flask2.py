# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:18:59 2021

@author: Nikitha
"""

from flask import Flask
from flask_restful import Api,Resource,reqparse,abort
app = Flask(__name__)
api = Api(app)

videos =   {
            1:{"name": "Niki","likes":10,"views":20},
            2:{"name": "Niks","likes":20,"views":25},
            3:{"name": "Piks","likes":30,"views":15}
            }

vid_args = reqparse.RequestParser()
vid_args.add_argument("name", type = str, help ="Name is required", required=True)
vid_args.add_argument("likes", type = int, help ="Likes is required", required=True)
vid_args.add_argument("views", type = int, help ="Views is required", required=True)

vid_put_args = reqparse.RequestParser()
vid_put_args.add_argument("name", type = str)
vid_put_args.add_argument("likes", type = int)
vid_put_args.add_argument("views", type = int)


class Videos(Resource):
    
   def get(self):
        return videos 
    
class single_Video_by_id(Resource):
    
   def get(self,video_id):
        return videos[video_id]
    
    
   def post(self, video_id):
       args=vid_args.parse_args()
       if video_id in videos:
           abort("Video already exists!!")
       videos[video_id] = {"name": args["name"],"likes" : args["likes"],"views" : args["views"]}
       return videos[video_id]
   
   def delete(self, video_id):
        if video_id not in videos:
            abort("Video does not exist")
        del videos[video_id]
           
   def put(self,video_id):
        args = vid_put_args.parse_args()
        if video_id not in videos:
            abort("Video does not exist")
        if args["name"]:
            videos[video_id]["name"]=args["name"]
        if args["likes"]:
            videos[video_id]["name"]=args["likes"]
        if args["views"]:
            videos[video_id]["name"]=args["views"]
        return videos[video_id]
            
api.add_resource(Videos, '/videos')
api.add_resource(single_Video_by_id, '/videos/<int:video_id>')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
    
    