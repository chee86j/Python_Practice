import { Fragment } from "react";
/*  
    Fragment from react is a component that allows you to group a list of children 
    w/o adding extra nodes to the DOM. In the Table component, Fragment is used 
    to wrap the custom header returned by column.header() w/o introducing an a
    dditional DOM element, ensuring the table structure remains correct while 
    allowing for flexible header content.
*/

/* Table is a reusable renderer that builds headers from config and rows from data.
   It checks for optional custom header functions, uses column render functions for each cell,
   and uses keyFn to assign stable keys for each generated row. */
function Table({ data, config, keyFn }) {
  const renderedHeaders = config.map((column) => {
    if (column.header) {
      return <Fragment key={column.label}>{column.header()}</Fragment>;
    }
    return <th key={column.label}>{column.label}</th>;
  });

  const renderedRows = data.map((rowData) => {
    const renderedCells = config.map((column) => {
      return (
        <td className="p-2" key={column.label}>
          {column.render(rowData)}
        </td>
      );
    });

    return (
      <tr className="border-b" key={keyFn(rowData)}>
        {renderedCells}
      </tr>
    );
  });

  return (
    <table className="table-auto border-spacing-2">
      <thead>
        <tr className="border-b-2">{renderedHeaders}</tr>
      </thead>
      <tbody>{renderedRows}</tbody>
    </table>
  );
}

export default Table;
