import { useState } from "react";

// useSort groups together the sorting state & sorting behavior so
// table components can reuse the same logic without duplicating it.
function useSort(data, config) {
  const [sortOrder, setSortOrder] = useState(null);
  const [sortBy, setSortBy] = useState(null);

  // handleSort cycles a column through ascending, descending, & unsorted.
  const handleSort = (label) => {
    if (sortBy && label !== sortBy) {
      setSortOrder("asc");
      setSortBy(label);
      return;
    }

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

  // The hook derives a sorted copy of the data from the current sort state.
  // If no column is selected, it returns the original data unchanged.
  let sortedData = data;
  if (sortOrder && sortBy) {
    const { sortValue } = config.find((column) => column.label === sortBy);

    sortedData = [...data].sort((a, b) => {
      const valueA = sortValue(a);
      const valueB = sortValue(b);
      const reverseOrder = sortOrder === "asc" ? 1 : -1;

      if (typeof valueA === "string") {
        return valueA.localeCompare(valueB) * reverseOrder;
      }

      return (valueA - valueB) * reverseOrder;
    });
  }

  // Return both the current sorting state & the function the component
  // will call when the user clicks a sortable column header.
  return {
    sortOrder,
    sortBy,
    sortedData,
    handleSort,
  };
}

export default useSort;
