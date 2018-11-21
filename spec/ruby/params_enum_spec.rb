# Autogenerated from KST: please remove this line if doing any edits by hand!

require 'params_enum'

RSpec.describe ParamsEnum do
  it 'parses test properly' do
    r = ParamsEnum.from_file('src/enum_0.bin')

    expect(r.one).to eq :animal_cat
    expect(r.invoke_with_param.is_cat).to eq true
  end
end