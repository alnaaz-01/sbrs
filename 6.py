class TravelExpert:
    def __init__(self):
        self.knowledge_base = {
            "destinations": {
                "paris": {
                    "description": "paris",
                    "currency": "ERU",
                    "price": 500,
                    "food": "ghhkjhj"
                },
                "america": {
                    "description": "paris",
                    "currency": "ERU",
                    "price": 500,
                    "food": "ghhkjhj"
                },
                "africa": {
                    "description": "paris",
                    "currency": "ERU",
                    "price": 500,
                    "food": "ghhkjhj"
                }
            }
        }

    def get_destination_info(self, destination):
        destination = destination.lower()
        if destination in self.knowledge_base["destinations"]:
            info = self.knowledge_base["destinations"][destination]["description"]
            currency = self.knowledge_base["destinations"][destination]["currency"]
            price = self.knowledge_base["destinations"][destination]["price"]
            food = self.knowledge_base["destinations"][destination]["food"]

            return f"{destination.capitalize()} \n Info :{info}\n Currency:{currency}\n Price:{price}\n food:{food}"
        else:
            return "sorry"

    def run(self):
        print("Welcome To travel Expert System")
        while True:
            user = input("Enter the destination would you like to learn (to quit enter 'exit'):-")
            if user == "exit":
                print("Goodbye")
                break
            response = self.get_destination_info(user)
            print("Travel Agent :-", response)


def main():
    travel = TravelExpert()
    travel.run()


if __name__ == "__main__":
    main()
