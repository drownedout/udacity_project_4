from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, CategoryItem

engine = create_engine('sqlite:///categoryitem.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Sports category
category1 = Category(name="Sports")

session.add(category1)
session.commit()

categoryItem2 = CategoryItem(name="Hockey Stick", description="Not for farming or assualt.",
                     category=category1)

session.add(categoryItem2)
session.commit()


categoryItem1 = CategoryItem(name="Basketball", description="Basket not included",
                     category=category1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name="Swim Goggles", description="Better than sunglasses and half the leakage!",
                     category=category1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(name="Helmet", description="You'll be the most popular person in your office",
                     category=category1)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(name="Fishing Rod", description="There's plenty of fish in the sea. Increase your odds of finding a hot date today!",
                     category=category1)

session.add(categoryItem4)
session.commit()

# Phones Category
category2 = Category(name="Phones")

session.add(category2)
session.commit()


categoryItem1 = CategoryItem(name="Samsung Galaxy Note 7", description="Now with less explosions and twice the fun!",
                     category=category2)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name="Iphone 8", description="Let's face it. You definitely need to buy another one. You wanna be cool, right?", category=category2)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(name="Windows Phone", description="Lol",
                     category=category2)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(name="Nokia 3310", description="For when you run out of concrete or need to make an improvisational bullet proof vest",
                     category=category2)

session.add(categoryItem4)
session.commit()


# Appliance category
category1 = Category(name="Appliances")

session.add(category1)
session.commit()


categoryItem1 = CategoryItem(name="Microwave", description="Don't stick your head in this one!",
                     category=category1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name="Dishwasher", description="Steve, I swear to God if this doesn't make you do your dishes I am leaving.",
                     category=category1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(name="Heater", description="To warm up that cold, black heart of yours.",
                     category=category1)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(name="Trash Can", description="For storing that collection of memoirs you wrote six years ago.",
                     category=category1)

session.add(categoryItem4)
session.commit()



# Pets Category
category1 = Category(name="Pets")

session.add(category1)
session.commit()


categoryItem1 = CategoryItem(name="Cat Toy", description="Let's be honest. Your cat is going to play with the box instead.",
                     category=category1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name="Kitty Litter", description="At least they don't go on the rug like your dog, Steve.",
                     category=category1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(name="Pet Shampoo", description="Comes with an extra 4 ounces for when your pet immediately runs into the mud after bathing.",
                     category=category1)

session.add(categoryItem3)
session.commit()


# Bikes category
category1 = Category(name="Bikes")

session.add(category1)
session.commit()


categoryItem1 = CategoryItem(name="Bike Light", description="This will likely be stolen within a week.",
                     category=category1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name="Bike Seat", description="You know what they say, a good bike seat is the best way to prevent an awkward conversation with you healthcare professional",
                     category=category1)

session.add(categoryItem2)
session.commit()

# Cars category
category1 = Category(name="Cars")

session.add(category1)
session.commit()


categoryItem1 = CategoryItem(name="Ford Pinto", description="Nothing says success like a Ford Pinto",
                     category=category1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name="Hummer H2", description="When you want to tell the world, 'Yes, I am compensating for something.'",
                     category=category1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(name="Car Oil", description="Not to be used for cooking.",
                     category=category1)

session.add(categoryItem3)
session.commit()


# Books Category
category1 = Category(name="Books")

session.add(category1)
session.commit()

categoryItem9 = CategoryItem(name="1984", description="George Orwell's dystopic vision of a future that happened over 20 years ago",
                     category=category1)

session.add(categoryItem9)
session.commit()


categoryItem1 = CategoryItem(name="A Brave New World", description="Does anyone know where I can get some SOMA? Asking for a friend.",
                     category=category1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name="House Of Leaves", description="A book about a book about a documentary.",
                     category=category1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(name="Of Mice And Men", description="Not featured - actual mice. Thanks a lot, Steinbeck.",
                    category=category1)

session.add(categoryItem3)
session.commit()


# Music Category
category1 = Category(name="Music")

session.add(category1)
session.commit()


categoryItem1 = CategoryItem(name="Guitar", description="Stun everyone when by learning to play the first three chords of 'Wonderwall'.",
                     category=category1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name="Bass", description="It's like a guitar but with none of the social benefits.",
                     category=category1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(name="Drums", description="Do you hate your neighbors? Then this will be a welcome addition to your household.",
                     category=category1)

session.add(categoryItem2)
session.commit()


print("Categories and items have been added")