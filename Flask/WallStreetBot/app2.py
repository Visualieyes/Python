from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import tweepy
import Keys_and_tokens
import os
import instabot
from PIL import Image

# twitter authentication
auth = tweepy.OAuthHandler(Keys_and_tokens.API_KEY, Keys_and_tokens.API_KEY_SECRET)
auth.set_access_token(Keys_and_tokens.ACCESS_TOKEN, Keys_and_tokens.ACCESS_TOKEN_SECRET)
twitterApi = tweepy.API(auth)

# instagram authentication
insta_user = Keys_and_tokens.INSTAGRAM_USERNAME
insta_pass = Keys_and_tokens.INSTAGRAM_PASSWORD


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == "POST":
        
        caption = request.form.get('caption', "")
        image = request.files.get('img', "")


        caption_insta = request.form.get('caption_insta', "")
        image_insta = request.files.get('img_insta', "")
        
        if len(caption) > 0 and str(image.headers).find("filename=\"\"") > 0:
            twitterApi.update_status(caption)
        elif caption == "" and image != "":
            if str(image.headers).find("image/jpeg") > 0 or str(image.headers).find("image/png") > 0:
                image.save(os.path.join("/home/ec2-user/project/postup/static/images/TwitterUploads/", "tmp.jpg"))
                twitterApi.update_with_media("static/images/TwitterUploads/"+"tmp.jpg")
                os.remove("static/images/TwitterUploads/tmp.jpg")
        elif len(caption) > 0 and (str(image.headers).find("image/jpeg") > 0 or str(image.headers).find("image/png") > 0):
            image.save(os.path.join("/home/ec2-user/project/postup/static/images/TwitterUploads/", "tmp.jpg"))
            twitterApi.update_with_media("static/images/TwitterUploads/"+"tmp.jpg", status=caption)
            os.remove("static/images/TwitterUploads/tmp.jpg")
        elif len(caption_insta) > 0 and str(image_insta.headers).find("filename=\"\"") > 0:
            #print("NEED IMAGE")
            return render_template("new_index2.html")
        elif caption_insta == "" and (str(image_insta.headers).find("image/jpeg") > 0 or str(image_insta.headers).find("image/png") > 0):
            image_insta.save(os.path.join("/home/ec2-user/project/postup/static/images/InstaUploads/", "tmp.jpg"))
            im = Image.open("static/images/InstaUploads/"+"tmp.jpg")
            img = im.convert('RGB') ###############################
            newsize = (1080, 1080)
            img = img.resize(newsize)
            img.save("static/images/InstaUploads/"+"tmp.jpg")
            bot = instabot.Bot()
            bot.login(username=insta_user, password=insta_pass, is_threaded=True)
            bot.upload_photo(photo="static/images/InstaUploads/"+"tmp.jpg")
            os.remove("static/images/InstaUploads/tmp.jpg.REMOVE_ME")
        elif len(caption_insta) > 0 and (str(image_insta.headers).find("image/jpeg") > 0 or str(image_insta.headers).find("image/png") > 0):
            image_insta.save(os.path.join("/home/ec2-user/project/postup/static/images/InstaUploads/", "tmp.jpg"))
            im = Image.open("static/images/InstaUploads/"+"tmp.jpg")
            img = im.convert('RGB') ################################
            newsize = (1080, 1080)
            img = img.resize(newsize)
            img.save("static/images/InstaUploads/"+"tmp.jpg")
            bot = instabot.Bot()
            bot.login(username=insta_user, password=insta_pass, is_threaded=True)
            bot.upload_photo(photo="static/images/InstaUploads/"+"tmp.jpg", caption=caption_insta)
            os.remove("static/images/InstaUploads/tmp.jpg.REMOVE_ME")
        else:
            return render_template("new_index2.html")
        return render_template("new_index2.html")

    return render_template("new_index2.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)