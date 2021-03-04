*** Settings ***
Documentation     Robo para pegar o link dos videos do site rede de canais
...               Deixar chrome e free download manager abertos para iniciar
Library           RPA.Desktop.Windows
Library           RPA.Desktop.Clipboard
Library           RPA.Images
Library           RPA.Browser
Library           MinhaLibExcel.py
Library           String
Task Setup        MinhaLibExcel.Open Application

*** Variables ***
${excelfile}=    COMPILADO.xlsx
${excelsheet}=    lista

*** Keywords ***
Old Tarefas no Navegador
    [Arguments]    ${urlep}
    Wait until keyword succeeds    3sec    0.1sec    Mouse click image    template=${EXECDIR}\\1604511071.bmp    off_x=100
    Copy to clipboard    ${urlep}
    Send keys to input    ^V    with_enter=true
    Wait until keyword succeeds    3sec    0.1sec    Mouse click image    template=${EXECDIR}\\1604512928.bmp    ctype=right
    Send keys    {DOWN}
    Send keys    {DOWN}
    Send keys    {DOWN}
    Send keys    {DOWN}
    Send keys    {DOWN}
    Send keys    {DOWN}
    Send keys    {ENTER}
    ${urldownload}=    Paste from clipboard
    Set global variable    ${urldownload}

*** Keywords ***
Tarefas no Navegador
    [Arguments]    ${urlep}
    Open Available Browser    ${urlep}
    ${urldownload}=    Get Element Attribute	css:body > div > div > a    href
    Set global variable    ${urldownload}
    Close Browser

*** Tasks ***
START Carregando info do excel
    Open Workbook           ${excelfile}
    Set Active Worksheet    sheetname=${excelsheet}
    #${lastrow}=    Find first available row
    #${lastrow}=    Evaluate    ${lastrow}[0]
    FOR    ${irow}    IN RANGE    2    123        #${lastrow}[0]
        ${urlep}=    Read from cells    row=${irow}    column=6
        Run keyword and continue on failure    Tarefas no Navegador    ${urlep}
        Run keyword and continue on failure    Write To Cells          row=${irow}    column=7    value=${urldownload}
    END
    Save Excel




