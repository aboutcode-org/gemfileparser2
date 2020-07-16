# gemfileparser2
Parse Ruby Gemfile's using Python. Supports Gemfiles, .gemspec and Cocoapods(.podspec) files. Friendly fork of https://gitlab.com/balasankarc/gemfileparser.

[gemfileparser](https://gitlab.com/balasankarc/gemfileparser) can only detect particular type of dependency in `.gemspec` files like it can detect only `s.add_development_dependency "rspec", "~>1.3.1"` or `s.add_runtime_dependency "rspec", "~>1.3.1"` type of dependency. Dependency should be in these 2 format only. 
[gemfileparser2](https://github.com/nexB/gemfileparser2) can detect all format of dependencies. This fork supports Gemfiles, .gemspec files and Cocoapods(.podspec) files.

### Installation
If using pip, use the command `sudo pip install gemfileparser2`  
Else use the following commands
```
git clone https://github.com/nexB/gemfileparser2.git
cd gemfileparser2
python setup.py install
```

### Usage
```
from gemfileparser2 import GemfileParser
parser = GemfileParser(<path to Gemfile>, <name of the application (optional)>)
dependency_dictionary = parser.parse()
```
The parse() method returns a dict object of the following format
```
{
'development': [list of dependency objects inside group 'development'],
'runtime': [list of runtime dependency objects],
.
.
.}
```
Each dependency object contains the following attributes
```
name - Name of the gem
requirement - Version requirement
autorequire - Autorequire value
source - Source URL of the gem
parent - Dependency of which gem
group - Group in which gem is a member of (default : runtime)
```

#### Example
```
from gemfileparser2 import GemfileParser
n = GemfileParser('Gemfile', 'diaspora')
deps = n.parse()
for key in deps:
   if deps[key]:
       print key
       for dependency in deps[key]:
           print "\t", dependency
```

### Copyright
2015-2018 Balasankar C <balasankarc@autistici.org>

### License
gemfileparser is dual-licensed under [GNU GPL version 3 (or above) License](http://www.gnu.org/licenses/gpl) and [MIT License](https://opensource.org/licenses/MIT).

Personally, I prefer anyone using this to respect the GPL license and use that
itself for derivative works - thus making them also Free Software. But, your
call.
