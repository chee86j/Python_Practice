import Button from "./Button.js";

function App() {
  return (
    <div>
      <div>
        <Button success primary rounded outline>
          Click me!!
        </Button>
      </div>
      <div>
        <Button danger outline>
          Buy Now!
        </Button>
      </div>
      <div>
        <Button warning>See Deal!</Button>
      </div>
      <div>
        <Button>Hide Ads!</Button>
      </div>
      <div>
        <Button>Sign Up!</Button>
      </div>
    </div>
  );
}

export default App;
