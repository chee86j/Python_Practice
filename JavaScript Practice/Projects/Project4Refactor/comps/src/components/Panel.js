// This is used to wrap the content of the page to minimize Tailwind CSS code
import className from 'classnames';

function Panel({ children, className, ...rest }) {
    const finalClassNames = className(
        'border rounded p-3 shadow bg-white w-full',
        className
    );
    return <div {...rest} className={finalClassNames}>{children}</div>;
}

export default Panel;