import ReactDOM from 'react-dom';
import { useEffect } from 'react';

function Modal({ onClose, children, actionBar }) {
    // Disable scrolling on the body when the modal is open
    useEffect(() => {
        document.body.classList.add('overflow-hidden');
        
        return () => {
            document.body.classList.remove('overflow-hidden');
        };
    }, []);

  return ReactDOM.createPortal(
    <div className="fixed inset-0 z-50">
      {/* Clicking the backdrop means the user clicked outside the modal therefore we close it. */}
      <div onClick={onClose} className="fixed inset-0 bg-gray-300 opacity-80"></div>
      <div
        className="fixed inset-40 bg-white p-10">
        <div className='flex flex-col justify-between h-full'>
            {children}
            <div className='flex justify-end'>
                {actionBar}
            </div>
        </div>
        
      </div>
    </div>,
    document.querySelector('.modal-container')
  );
}

export default Modal

/*  Goals
    1. The background overlay needs to cover the full screen, not just the page section.
    2. The modal should sit on top of everything else so existing content is blocked out.
    3. Render the modal with a portal so it mounts into `.modal-container` in index.html.
    4. Keep modal markup separate from the page layout so stacking and positioning stay predictable.

    Why we need portals
    - Portals allow us to render a component's JSX outside of its parent component's DOM hierarchy. 
    - This is useful for modals, tooltips, and other UI elements that need to visually break out of their parent container.
    - It provides a cleaner layering above the app content and avoids CSS complications that arise from nesting modals inside other components.
      i.e. z-index/stacking context issues, overflow:hidden on parent containers, etc.
    - This is the more predictable and safer way to implement modals in React.

*/
