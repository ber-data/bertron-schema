# bertron-schema

LinkML schema for BER data integration work

## Website

[https://ber-data.github.io/bertron-schema](https://ber-data.github.io/bertron-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [bertron_schema](src/bertron_schema)
    * [schema](src/bertron_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/bertron_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
To run commands you may use `make` or the command runner [just](https://github.com/casey/just/), which is a better choice on Windows.
Use the `make` command or `just` commands to generate project artefacts:
* `make help` or `just --list`: list all pre-defined tasks
* `make all` or `just all`: make everything
* `make deploy` or `just deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
