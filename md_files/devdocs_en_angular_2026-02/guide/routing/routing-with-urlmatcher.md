# Creating custom route matches

Creating custom route matches



# Creating custom route matches

  

The Angular Router supports a powerful matching strategy that you can use to help users navigate your application. This matching strategy supports static routes, variable routes with parameters, wildcard routes, and so on. Also, build your own custom pattern matching for situations in which the URLs are more complicated.

In this tutorial, you'll build a custom route matcher using Angular's [`UrlMatcher`](../../api/router/urlmatcher). This matcher looks for a Twitter handle in the URL.

## Objectives

Implement Angular's [`UrlMatcher`](../../api/router/urlmatcher) to create a custom route matcher.

## Create a sample application

Using the Angular CLI, create a new application, *angular-custom-route-match*. In addition to the default Angular application framework, you will also create a *profile* component.

1. Create a new Angular project, *angular-custom-route-match*.

   ```
   ng new angular-custom-route-match
   ```

   When prompted with `Would you like to add Angular routing?`, select `Y`.

   When prompted with `Which stylesheet format would you like to use?`, select `CSS`.

   After a few moments, a new project, `angular-custom-route-match`, is ready.
2. From your terminal, navigate to the `angular-custom-route-match` directory.
3. Create a component, *profile*.

   ```
   ng generate component profile
   ```
4. In your code editor, locate the file, `profile.component.html` and replace the placeholder content with the following HTML.

   ```
   <p>
       Hello {{ username() }}!
   </p>
   ```
5. In your code editor, locate the file, `app.component.html` and replace the placeholder content with the following HTML.

   ```
   <h2>Routing with Custom Matching</h2>

   Navigate to <a routerLink="/@Angular">my profile</a>

   <router-outlet />
   ```

## Configure your routes for your application

With your application framework in place, you next need to add routing capabilities to the `app.config.ts` file. As a part of this process, you will create a custom URL matcher that looks for a Twitter handle in the URL. This handle is identified by a preceding `@` symbol.

1. In your code editor, open your `app.config.ts` file.
2. Add an `import` statement for Angular's [`provideRouter`](../../api/router/providerouter) and [`withComponentInputBinding`](../../api/router/withcomponentinputbinding) as well as the application routes.

   ```
   import {provideRouter, withComponentInputBinding} from '@angular/router';

   import {routes} from './app.routes';
   ```
3. In the providers array, add a `provideRouter(routes, withComponentInputBinding())` statement.
4. Define the custom route matcher by adding the following code to the application routes.

   ```
   {
       matcher: (url) => {
         if (url.length === 1 && url[0].path.match(/^@[\w]+$/gm)) {
           return {consumed: url, posParams: {username: new UrlSegment(url[0].path.slice(1), {})}};
         }

         return null;
       },
       component: ProfileComponent,
     },
   ```

This custom matcher is a function that performs the following tasks:

- The matcher verifies that the array contains only one segment
- The matcher employs a regular expression to ensure that the format of the username is a match
- If there is a match, the function returns the entire URL, defining a `username` route parameter as a substring of the path
- If there isn't a match, the function returns null and the router continues to look for other routes that match the URL

**HELPFUL:** A custom URL matcher behaves like any other route definition. Define child routes or lazy loaded routes as you would with any other route.

## Reading the route parameters

With the custom matcher in place, you can now bind the route parameter in the `profile` component.

In your code editor, open your `profile.component.ts` file and create an [`input`](../../api/core/input) matching the `username` parameter. We added the [`withComponentInputBinding`](../../api/router/withcomponentinputbinding) feature earlier in [`provideRouter`](../../api/router/providerouter). This allows the [`Router`](../../api/router/router) to bind information directly to the route components.

```
username = input.required<string>();
```

## Test your custom URL matcher

With your code in place, you can now test your custom URL matcher.

1. From a terminal window, run the `ng serve` command.

   ```
   ng serve
   ```
2. Open a browser to `http://localhost:4200`.

   You should see a single web page, consisting of a sentence that reads `Navigate to my profile`.
3. Click the **my profile** hyperlink.

   A new sentence, reading `Hello, Angular!` appears on the page.

## Next steps

Pattern matching with the Angular Router provides you with a lot of flexibility when you have dynamic URLs in your application. To learn more about the Angular Router, see the following topics:

  [In-app Routing and Navigation](common-router-tasks)   [Router API](../../api/router/router)  

**HELPFUL:** This content is based on [Custom Route Matching with the Angular Router](https://medium.com/@brandontroberts/custom-route-matching-with-the-angular-router-fbdd48665483), by [Brandon Roberts](https://twitter.com/brandontroberts).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/routing/routing-with-urlmatcher>
