# Stop-Phishing

This little side-project has started as a response to huge phishing wave currently on going on discord. Basically this webapp works like this:

- You go to [This site](https://phishing.thredex.eu) and submit a phishing link
- Some administrator will verify the domain
- Domain will be saved in the database
- It will be optainable using an public API

## TODO

- Try to automate reporting abusive domain to registrar
- Find out if you can programmaticly report domain as phishing to google (so it is blocked by chrome at least)
- Create a discord bot that will delete phishing messages and maybe add a new ones to the existing database
- Create a public API to add new domains programmaticly
