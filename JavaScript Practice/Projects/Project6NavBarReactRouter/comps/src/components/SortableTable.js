import Table from './Table'

function SortableTable(props) {
    const { config } = props

    const updatedConfig = config.map((column) => {
        if (!column.sortValue) {
            return column
        }

        return {
            ...column,
            header: () => <th>{column.label} IS SORTABLE</th>
        }
    })

    return <Table {...props} />
}

export default SortableTable