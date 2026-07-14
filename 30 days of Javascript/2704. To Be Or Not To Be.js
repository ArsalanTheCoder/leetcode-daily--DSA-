var expect = function(val) {

    return {

        toBe: function(compareVal) {

            if (val === compareVal) {
                return true;
            }

            throw new Error("Not Equal");
        },

        notToBe: function(compareVal) {

            if (val !== compareVal) {
                return true;
            }

            throw new Error("Equal");
        }

    };

};


try {
    console.log(expect(5).toBe(null));
} catch (err) {
    console.log(err.message);
}