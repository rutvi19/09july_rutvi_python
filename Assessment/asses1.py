import datetime
users = {}  
posts = []  
def register_user():
   
    while True:
        uname = input("Enter new username: ")
        if not uname:
            print("Username cannot be blank!")
            continue
        if uname in users:
            print("Username already exists! Try another.")
            continue

        pwd = input("Enter password: ")
        if not pwd:
            print("Password cannot be blank!")
            continue

        users[uname] = pwd
        print(f"User '{uname}' registered successfully!")
        return


def login_user():
    for attempt in range(3):  
        uname = input("Enter username: ")
        password = input("Enter password: ")

        if uname in users and users[uname] == password:
            print(f"Login successful! Welcome, {uname}")
            return uname
        else:
            print("Invalid username or password. Try again.")

    print("Too many failed attempts. Exiting...")
    return None


def create_post(author):
    
    title = input("Enter post title: ")
    description = input("Enter post description: ")

    if not title or not description:
        print("Title/Description cannot be blank.")
        return

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    post = {
        "author": author,
        "title": title,
        "description": description,
        "date": date
    }
    posts.append(post)
    print("Post created successfully!")


def view_all_posts():
    if not posts:
        print(" No posts available.")
        return

    print("\n===== All Posts =====")
    for post in posts:
        print(f"\nAuthor: {post['author']}")
        print(f"Title : {post['title']}")
        print(f"Date  : {post['date']}")
        print(f"Desc  : {post['description']}")
    print("=====================\n")


def search_post():

    uname = input("Enter username to search posts: ")
    found = [p for p in posts if p["author"] == uname]

    if not found:
        print(f"📭 No posts found for user '{uname}'.")
        return

    print(f"\n===== Posts by {uname} =====")
    for post in found:
        print(f"\nTitle : {post['title']}")
        print(f"Date  : {post['date']}")
        print(f"Desc  : {post['description']}")
    print("==============================\n")


def main():
    while True:
        print("\n===== PostBoard Menu =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            user = login_user()
            if user:
                while True:
                    print("\n--- User Menu ---")
                    print("1. Create Post")
                    print("2. View All Posts")
                    print("3. Search Posts by Username")
                    print("4. Logout")

                    option = input("Choose an option: ")

                    if option == "1":
                        create_post(user)
                    elif option == "2":
                        view_all_posts()
                    elif option == "3":
                        search_post()
                    elif option == "4":
                        print(" Logged out.")
                        break
                    else:
                        print(" Invalid option. Try again.")
        elif choice == "3":
            print("Exiting PostBoard. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()