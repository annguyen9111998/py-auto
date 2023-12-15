[CmdletBinding()]
param (
    $browser,
    $environment,
    $tag
)

$browser = $browser
$env = $environment
$tag = $tag
$tag_command = ""
if(-Not ($tag -eq "NA")){$tag_command='-m "' + $tag + '"'}
cd .\DemoQABookStore
pytest --alluredir=allure_report --junitxml=report.xml $tag_command --browser $browser --test-env $env .\testcases\ui\test_login.py