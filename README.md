# Word	Search
## A HTTP	service	that	provides	an	endpoint	for	fuzzy	search	/	autocomplete	of	English	words.
- Intially I uploaded the datasets in to default Django database.
- Created the search endpoint "search" for querying.
- Basic	input	search box is created in	the	frontend	which	calls	your	API	endpoint	on	the	backend	when	some	input	is typed	in	it.
## Setting the environment
- First set up the virtual environment to install Django with the below commands.
```bash
>cd Desktop/project/
> python3 -m venv ./venv
```
- To activate the virtual environment, navigate to Scripts directory with the below commands.
```bash
> cd venv/Scripts
> activate.bat
```
- Install django and other requirements using the below commands.
```bash
>cd Desktop/project/
> pip install django
```
- After installation, download the project from above repository and extract it in the project folder.
- Run the django server to enable the application with the below command.
```
> cd webassignment
> python manage.py runserver
```
- Open your favorite browser to view the results with the below url and this will take you to home page where you can upload your data in .tsv format if you have.
```bash
localhost:8000
```
- For searching words use the below url, which takes you to search page.
```bash
localhost:8000/search/
```
**NOTE: While setting up the environment or running the application, if you face any challenges please feel free to contact me.**
