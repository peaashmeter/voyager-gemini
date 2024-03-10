from voyager import Voyager
from key import google_api_key

voyager = Voyager(
    mc_port=54321,
    google_api_key=google_api_key,
    resume=False,
)   

# start lifelong learning
voyager.learn()
