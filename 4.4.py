people =
2 [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
3 {'first':'Barack', 'last':'Obama', 'email':'president@whitehouse.gov'},
4 {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}
5 ]

LastName, FirstName: email@example.com

for person in sorted(people, key=lambda person: [person['last'], person['first']]):
2 print("{last}, {first}: {email}".format(**person))