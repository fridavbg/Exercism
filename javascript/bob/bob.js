//
// This is only a SKELETON file for the 'Bob' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const responses = {
    question: "Sure.",
    yell: "Whoa, chill out!",
    questionYelled: "Calm down, I know what I'm doing!",
    silence: "Fine. Be that way!",
    default: "Whatever.",
};

export const hey = (message) => {
    let response = responses.default;
    let isQuestion = message.trim().endsWith("?");
    const isYelling =
        message.toUpperCase() === message && /[A-Za-z]/.test(message);

    if (isQuestion && isYelling) {
        response = responses.questionYelled;
    } else if (isQuestion) {
        response = responses.question;
    } else if (isYelling) {
        response = responses.yell;
    } else if (message.trim() === "") {
        response = responses.silence;
    }

    return response;
};
