# Scraping Criminal Statistics

Extraction of criminal statistics from the Goiás state government portal.

## References

- [Goiás State Statistics Portal](https://seguranca.go.gov.br/estatisticas)
- [tabula-py](https://tabula-py.readthedocs.io/en/latest/)
- [Camelot](https://camelot-py.readthedocs.io/en/master/)
- [Excalibur](https://excalibur-py.readthedocs.io/en/master/)

## Examples

- [tabula-py example notebook](https://nbviewer.jupyter.org/github/chezou/tabula-py/blob/master/examples/tabula_example.ipynb)

## Tools

### tabula-py

**Dependencies**

```sh
pip install tabula-py
```

**REPL**

```py
>>> import tabula
>>>
>>> file = 'https://www.seguranca.go.gov.br/wp-content/uploads/2020/11/relatorio-2020-jan-e-set.pdf'
>>>
>>> tables = tabula.read_pdf(file, pages='all', multiple_tables=True, stream=True)
>>>
>>> tabula.convert_into(file, './tabula_tables.csv', output_format='csv', pages='all')
>>> exit()
```

### Camelot

**Dependencies**

- [Ghostscript](https://github.com/brunowego/cookbooks/blob/develop/ghostscript.md)

```sh
pip install camelot-py opencv-python
```

**REPL**

```py
>>> import camelot
>>>
>>> file = 'https://www.seguranca.go.gov.br/wp-content/uploads/2020/11/relatorio-2020-jan-e-set.pdf'
>>>
>>> tables = camelot.read_pdf(file, pages='1-end', flavor='stream')
>>>
>>> tables[0].df
>>> tables[0].parsing_report
>>>
>>> tables.export('./camelot_tables.csv', f='csv')
>>> exit()
```

### Excalibur

**Dependencies**

- [Ghostscript](https://github.com/brunowego/cookbooks/blob/develop/ghostscript.md)

**Running Web Server**

```sh
pip install excalibur-py

# Change to use '~/.excalibur' folder instead of '~/excalibur'
export EXCALIBUR_HOME="$HOME/.excalibur"

# Initialize locally database
excalibur initdb

# Run web server
excalibur webserver

# Open on web browser
echo -e '[INFO]\thttp://127.0.0.1:5000'
```
