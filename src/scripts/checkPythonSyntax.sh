#!/bin/bash
doCheckPythonSyntax() {

    source_dir=$1

    echo "Python source directory is $source_dir"
    cd $source_dir

    while read -r f ; do \

        py_path_ext=$f
        py_name=${py_name_ext%.*}

        echo "Python file to check: $py_path_ext"
        python -m py_compile $py_path_ext

        if test $? -ne 0; then
            echo "Python scripts compilation failed"
            exit 1
        fi

    done< <(find "$source_dir" -type f -name "*.py")

}

doCheckPythonSyntax $1
exit 0