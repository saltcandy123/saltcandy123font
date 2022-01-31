import React from "react";
import App, { AppProps } from "next/app";
import Head from "next/head";
import { createTheme, CssBaseline, ThemeProvider } from "@mui/material";
import "@src/fonts.css";

const theme = createTheme({
  typography: {
    fontSize: 16,
    fontFamily: '"saltcandy123font"',
  },
});

const CustomApp: React.FunctionComponent<AppProps> = (props) => {
  return (
    <>
      <Head>
        <title>saltcandy123font</title>
        <meta name="robots" content="noindex" />
        <meta name="viewport" content="initial-scale=1, width=device-width" />
      </Head>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <App {...props} />
      </ThemeProvider>
    </>
  );
};

export default CustomApp;
