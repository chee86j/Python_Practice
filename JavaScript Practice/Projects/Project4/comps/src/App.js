import Button from "./Button.js";

function App() {
  return (
    <div>
      <div>
        <Button outline rounded>
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
        <Button secondary outline>
          Hide Ads!
        </Button>
      </div>
      <div>
        <Button primary rounded>
          Sign Up!
        </Button>
      </div>
    </div>
  );
}

export default App;
