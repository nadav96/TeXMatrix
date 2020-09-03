#!/usr/local/bin/python3
import json

output = {}
for rows in range(1, 13):
    for cols in range(1, 13):
        matrix_output = {
            "prefix": ["{}x{};matrix".format(rows,cols), "row={},col={};matrix".format(rows,cols)],
            "description": "{} by {} matrix".format(rows, cols)
        }
        body = ["\\begin{bmatrix}"]

        # add the matrix body
        cell_count = 1
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append("{}{}{}".format("${", cell_count, ":({},{}){}".format(i,j, "}")))
                cell_count += 1
            raw_row = " & ".join(row)
            raw_row = "\t{}\\\\\\".format(raw_row)
            body.append(raw_row)

        body.append("\\end{bmatrix}")

        matrix_output["body"] = body

        output["matrix:{}x{}".format(rows,cols)] = matrix_output

with open("./snippets.json", "w") as fw:
    json.dump(output, fw)
print(output)