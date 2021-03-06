import * as fs from "fs";
import * as path from "path";
import React from "react";
import { GetStaticProps, NextPage } from "next";
import {
  Card,
  CardContent,
  CardHeader,
  Grid,
  makeStyles,
  Typography,
} from "@material-ui/core";
import { Layout } from "@src/layout";

const useStyles = makeStyles((theme) => ({
  glyph: {
    width: theme.typography.fontSize * 4,
  },
  glyphHeader: {
    padding: theme.spacing(0.25, 0),
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.contrastText,
    textAlign: "center",
  },
  glyphHeaderContent: {
    fontSize: theme.typography.fontSize * 0.75,
    fontFamily: "sans-serif",
  },
  glyphContent: {
    padding: 0,
    paddingBottom: 0,
    fontSize: theme.typography.fontSize * 2,
    textAlign: "center",
    "&:last-child": {
      padding: 0,
    },
  },
}));

const Glyph: React.FunctionComponent<{ charCode: number }> = (props) => {
  const styles = useStyles();
  // workaround to force to show a space (0x20)
  const char =
    props.charCode === 0x20 ? "\u00a0" : String.fromCodePoint(props.charCode);
  const hex = props.charCode.toString(16);
  const codeText = `u${"0000".substring(hex.length)}${hex}`;

  return (
    <Card classes={{ root: styles.glyph }}>
      <CardHeader
        classes={{ root: styles.glyphHeader, title: styles.glyphHeaderContent }}
        title={
          <>
            <div>{codeText}</div>
            <div>{char}</div>
          </>
        }
      />
      <CardContent className={styles.glyphContent}>{char}</CardContent>
    </Card>
  );
};

interface GlyphsPageProps {
  charCodes: number[];
}

const GlyphsPage: NextPage<GlyphsPageProps> = (props) => {
  return (
    <Layout>
      <Typography variant="h3" component="h1" gutterBottom>
        Glyphs
      </Typography>
      <Grid container spacing={1}>
        {props.charCodes.map((charCode) => (
          <Grid key={charCode} item>
            <Glyph charCode={charCode} />
          </Grid>
        ))}
      </Grid>
    </Layout>
  );
};

export const getStaticProps: GetStaticProps<GlyphsPageProps> = async () => {
  const basePath = path.join(process.cwd(), "../glyphs");
  const charCodes = fs
    .readdirSync(basePath)
    .filter((filename) => /^u[0-9a-f]{4}\.svg$/.test(filename))
    .map((filename) => parseInt(filename.substring(1, 5), 16))
    .sort((a, b) => a - b);
  return {
    props: {
      charCodes,
    },
  };
};

export default GlyphsPage;
