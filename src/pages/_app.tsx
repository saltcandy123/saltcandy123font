import React from "react";
import App, { AppProps } from "next/app";
import Head from "next/head";
import { createTheme, CssBaseline, ThemeProvider } from "@material-ui/core";
import "@src/fonts.css";

const theme = createTheme({
  typography: {
    fontSize: 16,
    fontFamily: "DemoFont",
  },
});

const CustomApp: React.FunctionComponent<AppProps> = (props) => {
  // See https://material-ui.com/guides/server-rendering/
  React.useEffect(() => {
    const jssStyles = document.querySelector("#jss-server-side");
    jssStyles?.parentElement?.removeChild(jssStyles);
  }, []);

  return (
    <>
      <Head>
        <title>saltcandy123font</title>
        <meta name="robots" content="noindex" />
      </Head>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <App {...props} />
      </ThemeProvider>
    </>
  );
};

export default CustomApp;
