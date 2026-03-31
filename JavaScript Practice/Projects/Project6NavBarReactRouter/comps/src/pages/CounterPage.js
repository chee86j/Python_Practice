import Button from "../components/Button";
import useCounter from "../hooks/use-Counter";

/* CounterPage shows the usual custom-hook workflow:
   1. Identify stateful logic that belongs together.
   2. Move that logic into a function whose name starts with "use".
   3. Pass in any values the logic needs, like initialCount.
   4. Return the state and helper functions the component should use.
   The result is reusable logic without duplicating the same useState/useEffect code in multiple components.
*/

// Original Code

// function CounterPage({ initialCount }) {
//   const [count, setCount] = useState(initialCount);

//   useEffect(() => {
//     console.log(count);
//   }, [count]);

//   const handleClick = () => {
//     setCount(count + 1);
//   };

//   return (
//     <div>
//       <h1>Count is {count} </h1>
//       <Button onClick={handleClick}>Increment</Button>
//     </div>
//   );
// }

function CounterPage({ initialCount }) {
  // The hook gives this component the current count plus the increment behavior.
  const [count, increment] = useCounter(initialCount);

  return (
    <div>
      <h1>Count is {count} </h1>
      <Button onClick={increment}>Increment</Button>
    </div>
  );
}

export default CounterPage;
