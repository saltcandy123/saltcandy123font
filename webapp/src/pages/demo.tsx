import React, { useState } from "react";
import { NextPage } from "next";
import { Box, makeStyles, TextField, Typography } from "@material-ui/core";
import { Layout } from "@src/layout";

const useStyles = makeStyles({
  textField: {
    fontFamily: "sans-serif",
  },
  textPreview: {
    wordBreak: "break-word",
  },
});

const TablePage: NextPage = () => {
  const styles = useStyles();
  const [text, setText] = useState<string>("");

  return (
    <Layout>
      <Typography variant="h3" component="h1" gutterBottom>
        Demo
      </Typography>
      <Box mb={4}>
        <TextField
          multiline
          fullWidth
          variant="filled"
          label="Type something here"
          InputLabelProps={{ className: styles.textField }}
          InputProps={{ className: styles.textField }}
          onChange={(e) => setText(e.target.value)}
        />
      </Box>
      <Typography variant="h5" component="p" className={styles.textPreview}>
        {text
          .split("\n")
          .map((line, idx) => [idx > 0 && <br key={idx} />, line])}
      </Typography>
    </Layout>
  );
};

export default TablePage;
