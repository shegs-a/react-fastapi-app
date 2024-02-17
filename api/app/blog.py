from fastapi import APIRouter
from decouple import Choices, config

LESSON_DAY = config(
    "HNG_LESSON_DAY",
    default="day1",
    cast=Choices([
        "day1",
        "day2",
        "day3",
        "day4",
        "day5",
        "day6",
    ])
)

app = APIRouter(tags=["Blogs"], prefix=f"/{LESSON_DAY}")
blogs = [
    {
        "id": "1",
        "slug": "docker-and-kubernetes-crash-course",
        "title": "Docker and Kubernetes Crash Course",
        "summary": """This is a two week crash course in Docker and Kubernetes.
            It would require about 2 hours every day (3 days a week).
            You will be taught, and given practical exercises that allows you
            learn the fundamentals of containerisation.
            The lessons would be about 20 minutes of theory, 20 minutes of
            practical, 20 minutes of q and a, then an exercise that you will
            do. Your work would be graded and feedback given. All lessons will
            be recorded for later review. This course is ONLY for people with
            existing knowledge in backend, frontend or DevOps. It is not a
            beginners course, and the material will not be appropriate for
            people who are not already coders!
            If you successfully complete the course and pass the final exam,
            N2k will be paid to you! A certificate will also be issued to you.
            """,
        "body": """The Body of the Blog should be long
            But I am too lazy to type, so I will fill it with lorem ipsum
            Lorem ipsum dolor sit amet, consectetur adipiscing elit,
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
            """
    }
]


@app.get("/list-blogs")
async def get_all_blogs() -> dict:
    print(LESSON_DAY)
    return {"data": blogs}


@app.get("/blog/{slug}")
async def get_blog_by_slug() -> dict:
    return {""}
