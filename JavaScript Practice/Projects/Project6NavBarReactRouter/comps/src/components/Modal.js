import ReactDOM from 'react-dom';

function Modal() {
    return ReactDOM.createPortal (
        <div>
        <div className='absolute inset-0 bg-gray-300 opacity-80'></div>
        <div className='absolute inset-40 p-10 bg-white'>I'm a modal</div>
    </div>,
    document.querySelector('.modal-container')
    )
}

export default Modal

/*  Goals
    1. The background overlay needs to cover the full screen, not just the page section.
    2. The modal should sit on top of everything else so existing content is blocked out.
    3. Render the modal with a portal so it mounts into `.modal-container` in index.html.
    4. Keep modal markup separate from the page layout so stacking and positioning stay predictable.
*/
