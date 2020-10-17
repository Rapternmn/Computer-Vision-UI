import { makeStyles } from '@material-ui/core/styles';

export const useStyles = makeStyles(theme => ({
    
    cardGrid: {
        paddingTop: theme.spacing(8),
        paddingBottom: theme.spacing(8),
    },
    card: {
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
    },
    cardJson: {
        display: 'flex',
        flexDirection: 'column',
    },
    cardMedia: {
        paddingTop: '100%',
        flexGrow: 1,
    },
    cardContent: {
        flexGrow: 1,
    },
}));