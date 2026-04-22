# Testing Pipes

Testing Pipes



# Testing Pipes

  

You can test [pipes](../templates/pipes) without the Angular testing utilities.

## Testing the TitleCasePipe

A pipe class has one method, `transform`, that manipulates the input value into a transformed output value. The `transform` implementation rarely interacts with the DOM. Most pipes have no dependence on Angular other than the [`@Pipe`](../../api/core/pipe) metadata and an interface.

Consider a [`TitleCasePipe`](../../api/common/titlecasepipe) that capitalizes the first letter of each word. Here's an implementation with a regular expression.

```
import {Pipe, PipeTransform} from '@angular/core';

@Pipe({name: 'titlecase', pure: true})
/** Transform to Title Case: uppercase the first letter of the words in a string. */
export class TitleCasePipe implements PipeTransform {
  transform(input: string): string {
    return input.length === 0
      ? ''
      : input.replace(/\w\S*/g, (txt) => txt[0].toUpperCase() + txt.slice(1).toLowerCase());
  }
}
```

Anything that uses a regular expression is worth testing thoroughly. You can use standard unit testing techniques to explore the expected cases and the edge cases.

```
describe('TitleCasePipe', () => {
  // This pipe is a pure, stateless function so no need for BeforeEach
  const pipe = new TitleCasePipe();

  it('transforms "abc" to "Abc"', () => {
    expect(pipe.transform('abc')).toBe('Abc');
  });

  it('transforms "abc def" to "Abc Def"', () => {
    expect(pipe.transform('abc def')).toBe('Abc Def');
  });

  // ... more tests ...
});
```

## Writing DOM tests to support a pipe test

These are tests of the pipe *in isolation*. They can't tell if the [`TitleCasePipe`](../../api/common/titlecasepipe) is working properly as applied in the application components.

Consider adding component tests such as this one:

```
it('should convert hero name to Title Case', async () => {
      harness.fixture.autoDetectChanges();
      // get the name's input and display elements from the DOM
      const hostElement: HTMLElement = harness.routeNativeElement!;
      const nameInput: HTMLInputElement = hostElement.querySelector('input')!;
      const nameDisplay: HTMLElement = hostElement.querySelector('span')!;

      // simulate user entering a new name into the input box
      nameInput.value = 'quick BROWN  fOx';

      // Dispatch a DOM event so that Angular learns of input value change.
      nameInput.dispatchEvent(new Event('input'));

      // Wait for Angular to update the display binding through the title pipe
      await harness.fixture.whenStable();

      expect(nameDisplay.textContent).toBe('Quick Brown  Fox');
    });
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/testing/pipes>
