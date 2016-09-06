9/6

Current status
------------------------
- Slack signup
- Github signup

- learnpython.org
- try.git


New Github repo
----------------------
- make repo
- use default rename, .gitignore, license

Using pycharm
----------------------
- clone project
- setup interpreter / create conda env


Using conda
------------------------
- installed?
- conda create -nmyenv pip
- source activate myenv

- note path for `setup interpreter`
- make two different envs and switch between them


Common Do's/Don'ts
- string assembly
  ```
  # do
  new_str = 'this is a {} formatted string => {}'.format(desc, myvar)
  
  # dont
  new_str = 'this is a'+' poorly '+ 'formatted string => '+'some text'
  ```
- path assembly
  ```
  # do
  new_path = os.path.join(a,b,c)
  
  # dont
  new_path = '/Users/ross/Documents/data/foo/bar'
  
  # easy way to get "home" folder
  home = os.path.expandusr('~')
  ```
- opening a file
  ```
  # do
  with open(path_to_file, 'r') as rfile:
    for line in rfile:
      print line.strip()
      
  # dont
  rfile = open(path_to_file,'r')
  
  DIGRESSION: remember files are iterable. Sooo
  
  # do
  for line in rfile:
    ...
    
  # dont'
  lines = rfile.readlines()
  for line in lines:
    ...
  ```
  
