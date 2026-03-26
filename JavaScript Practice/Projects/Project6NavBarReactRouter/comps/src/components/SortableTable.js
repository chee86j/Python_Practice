import { useState } from "react";
import Table from "./Table";

function SortableTable(props) {
  const [sortOrder, setSortOrder] = useState(null);
  const [sortBy, setSortBy] = useState(null);
  const { config } = props;

  /* 
     This is our updated list of config objects that we will pass to the Table 
     component. We map over the original config & check if each column has a 
     sortValue function. If it does, we create a new column object that includes 
     a custom header function which returns a <th> element with the label & an 
     indication that it's sortable. If the column doesn't have a sortValue, we 
     return it unchanged. 
    */

  const handleClick = (label) => {
    if (sortOrder === null) {
      setSortOrder("asc");
      setSortBy(label);
    } else if (sortOrder === "asc") {
      setSortOrder("desc");
      setSortBy(label);
    } else if (sortOrder === "desc") {
      setSortOrder(null);
      setSortBy(null);
    }
  };

  const updatedConfig = config.map((column) => {
    if (!column.sortValue) {
      return column;
    }

    return {
      ...column,
      header: () => (
        <th onClick={() => handleClick(column.label)}>
          {column.label} IS SORTABLE
        </th>
      ),
    };
  });

  return (
    <div>
      {sortOrder} - {sortBy}
      <Table {...props} config={updatedConfig} />;
    </div>
  );
  // the secondary config argument will overwrite the original config in {...props} when passed to Table, allowing us to inject our custom headers for sortable columns without modifying the original config object.
}

export default SortableTable;
