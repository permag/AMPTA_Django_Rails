class AddPasswordDigestColumnUsersTable < ActiveRecord::Migration
  def change
    add_column :users, :password_digist, :string
  end
end
