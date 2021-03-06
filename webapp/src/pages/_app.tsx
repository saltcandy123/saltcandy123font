import React, { useEffect } from "react";
import App, { AppProps } from "next/app";
import Head from "next/head";
import { useRouter } from "next/router";
import { createMuiTheme, CssBaseline, ThemeProvider } from "@material-ui/core";
import "@src/fonts.css";

const theme = createMuiTheme({
  typography: {
    fontSize: 18,
    fontFamily: "DemoFont",
  },
});

const CustomApp: React.FunctionComponent<AppProps> = (props) => {
  const router = useRouter();

  // See https://material-ui.com/guides/server-rendering/
  useEffect(() => {
    const jssStyles = document.querySelector("#jss-server-side");
    jssStyles?.parentElement?.removeChild(jssStyles);
  }, []);

  return (
    <>
      <Head>
        <title>saltcandy123font</title>
        {router.pathname !== "/" && <meta name="robots" content="noindex" />}
      </Head>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <App {...props} />
      </ThemeProvider>
    </>
  );
};

export default CustomApp;
