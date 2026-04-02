import { useEffect, useState } from "react";

// useCounter packages count state, its side effect, and the increment action
// so any component can reuse that logic by calling the hook.
function useCounter(initialCount) {
  const [count, setCount] = useState(initialCount);

  useEffect(() => {
    console.log(count);
  }, [count]);

  const increment = () => {
    setCount((currentCount) => currentCount + 1);
  };

  return [count, increment];
}

export default useCounter;
